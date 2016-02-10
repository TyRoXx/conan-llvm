from conans import ConanFile
import os, shutil
from conans.tools import download, unzip, check_sha256
from conans import CMake
from glob import glob

class LLVMConan(ConanFile):
    name = "llvm"
    version = "3.7.1"
    branch = "stable"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "zlib/1.2.8@lasote/stable"
    url="http://github.com/TyRoXx/conan-llvm"
    ZIP_FOLDER_NAME = "llvm-3.7.1.src"

    def source(self):
        zip_name = "llvm-3.7.1.src.tar.xz"
        
        download("http://llvm.org/releases/3.7.1/%s" % zip_name, zip_name)
        check_sha256(zip_name, "be7794ed0cec42d6c682ca8e3517535b54555a3defabec83554dbc74db545ad5")
        
        self.run("tar -xJf %s" % zip_name)
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self.settings)
        self.run("mkdir build")
        self.run("mkdir install")
        self.run('cd build && cmake ../%s -DCMAKE_INSTALL_PREFIX=%s %s' % (self.ZIP_FOLDER_NAME, "../install", cmake.command_line))
        self.run("cd build && cmake --build . %s -- install -j12" % cmake.build_config)
        
    def package(self):
        self.copy("*", "include", "install/include", keep_path=True)
        self.copy(pattern="*.a", dst="lib", src="install/lib", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="install/lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['libLLVMLTO.a', 'libLLVMObjCARCOpts.a', 'libLLVMLinker.a', 'libLLVMBitWriter.a', 'libLLVMIRReader.a', 'libLLVMXCoreDisassembler.a', 'libLLVMXCoreCodeGen.a', 'libLLVMXCoreDesc.a', 'libLLVMXCoreInfo.a', 'libLLVMXCoreAsmPrinter.a', 'libLLVMSystemZDisassembler.a', 'libLLVMSystemZCodeGen.a', 'libLLVMSystemZAsmParser.a', 'libLLVMSystemZDesc.a', 'libLLVMSystemZInfo.a', 'libLLVMSystemZAsmPrinter.a', 'libLLVMSparcDisassembler.a', 'libLLVMSparcCodeGen.a', 'libLLVMSparcAsmParser.a', 'libLLVMSparcDesc.a', 'libLLVMSparcInfo.a', 'libLLVMSparcAsmPrinter.a', 'libLLVMPowerPCDisassembler.a', 'libLLVMPowerPCCodeGen.a', 'libLLVMPowerPCAsmParser.a', 'libLLVMPowerPCDesc.a', 'libLLVMPowerPCInfo.a', 'libLLVMPowerPCAsmPrinter.a', 'libLLVMNVPTXCodeGen.a', 'libLLVMNVPTXDesc.a', 'libLLVMNVPTXInfo.a', 'libLLVMNVPTXAsmPrinter.a', 'libLLVMMSP430CodeGen.a', 'libLLVMMSP430Desc.a', 'libLLVMMSP430Info.a', 'libLLVMMSP430AsmPrinter.a', 'libLLVMMipsDisassembler.a', 'libLLVMMipsCodeGen.a', 'libLLVMMipsAsmParser.a', 'libLLVMMipsDesc.a', 'libLLVMMipsInfo.a', 'libLLVMMipsAsmPrinter.a', 'libLLVMHexagonDisassembler.a', 'libLLVMHexagonCodeGen.a', 'libLLVMHexagonDesc.a', 'libLLVMHexagonInfo.a', 'libLLVMCppBackendCodeGen.a', 'libLLVMCppBackendInfo.a', 'libLLVMBPFCodeGen.a', 'libLLVMBPFDesc.a', 'libLLVMBPFInfo.a', 'libLLVMBPFAsmPrinter.a', 'libLLVMARMDisassembler.a', 'libLLVMARMCodeGen.a', 'libLLVMARMAsmParser.a', 'libLLVMARMDesc.a', 'libLLVMARMInfo.a', 'libLLVMARMAsmPrinter.a', 'libLLVMAMDGPUCodeGen.a', 'libLLVMAMDGPUAsmParser.a', 'libLLVMAMDGPUUtils.a', 'libLLVMAMDGPUDesc.a', 'libLLVMAMDGPUInfo.a', 'libLLVMAMDGPUAsmPrinter.a', 'libLLVMAArch64Disassembler.a', 'libLLVMAArch64CodeGen.a', 'libLLVMAArch64AsmParser.a', 'libLLVMAArch64Desc.a', 'libLLVMAArch64Info.a', 'libLLVMAArch64AsmPrinter.a', 'libLLVMAArch64Utils.a', 'libLLVMMIRParser.a', 'libLLVMAsmParser.a', 'libLLVMLibDriver.a', 'libLLVMOption.a', 'libLLVMDebugInfoPDB.a', 'libLLVMTableGen.a', 'libLLVMOrcJIT.a', 'libLLVMLineEditor.a', 'libLLVMX86Disassembler.a', 'libLLVMX86AsmParser.a', 'libLLVMX86CodeGen.a', 'libLLVMSelectionDAG.a', 'libLLVMAsmPrinter.a', 'libLLVMX86Desc.a', 'libLLVMMCDisassembler.a', 'libLLVMX86Info.a', 'libLLVMX86AsmPrinter.a', 'libLLVMX86Utils.a', 'libLLVMMCJIT.a', 'libLLVMDebugInfoDWARF.a', 'libLLVMPasses.a', 'libLLVMipo.a', 'libLLVMVectorize.a', 'libLLVMInterpreter.a', 'libLLVMExecutionEngine.a', 'libLLVMRuntimeDyld.a', 'libLLVMCodeGen.a', 'libLLVMTarget.a', 'libLLVMScalarOpts.a', 'libLLVMProfileData.a', 'libLLVMObject.a', 'libLLVMMCParser.a', 'libLLVMBitReader.a', 'libLLVMInstCombine.a', 'libLLVMInstrumentation.a', 'libLLVMTransformUtils.a', 'libLLVMipa.a', 'libLLVMMC.a', 'libLLVMAnalysis.a', 'libLLVMCore.a', 'libLLVMSupport.a']
        if not self.settings.os == "Windows":
            self.cpp_info.libs.append("pthread")
            self.cpp_info.libs.append("dl")
            self.cpp_info.libs.append("tinfo")
