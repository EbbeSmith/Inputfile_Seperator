import os
from abaqus import * 
from abaqusConstants import * 

def splitInputFile(inputFile):
    
    """ Check if file exists """
    if os.path.isfile(inputFile) == False:
        print("%s is not found" % inputFile) 
        return 
        
    """ Open File and Remove Keywords """ 
    outputFile = inputFile.replace('.inp', '_analysis.inp')
    fout = open(outputFile, 'w')
    fin = open(inputFile, 'r')
    
    """ Parse the Lines and Ignore datalines if one of the ignoreKwds appears""" 
    ignoreKwds = ['*Node\n','*Element,','*Nset,', '*Elset,']
    copyFlag = True
    for line in fin.readlines():   
        if '*' in line and not '**' in line:
            print(line.replace('\n', ''))
            if line.split(' ')[0] in ignoreKwds:
                copyFlag = False
                fout.write(line)  # Write the Kwyword itself! 
                print("--------NOT COPY THESE LINES-----------")
            else:
                copyFlag = True
                   
        if copyFlag:
            fout.write(line)
        
    fin.close()
    fout.close() 
    return

def main(): 
    """ Create a Job for the current """
    model =  mdb.models[session.sessionState[session.currentViewportName]['modelName']]
    job = mdb.Job(name="splitInp", model=model.name)
    job.writeInput()
    del mdb.jobs[job.name]

    fileName = os.getcwd()+"\splitInp.inp"
    splitInputFile(fileName)

    # Ask to run file...
    runJob = getWarningReply('Run Job with subprocess?\n', (YES,NO))
    if runJob == YES:
        print("Delete Old Job If it exists")
        print("Import job")
        print("Submit Job")
    return True


""" Allow the script to be run natively as file->run Script"""
if __name__ == '__main__':
    main() 