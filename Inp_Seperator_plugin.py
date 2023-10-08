from abaqusGui import getAFXApp
from abaqusConstants import * 
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()

#import Inp_Seperator_kernel
#reload(Inp_Seperator_kernel)

toolset.registerKernelMenuButton(
	buttonText = 'Inputfiles | Create and Seperate Inputfile from Current Model', 
	moduleName = 'Inp_Seperator_dev', 
    functionName ='main()' )