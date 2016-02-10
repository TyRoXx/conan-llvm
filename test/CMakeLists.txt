project(llvm_test)
cmake_minimum_required(VERSION 2.8)

include(conanbuildinfo.cmake)
conan_basic_setup()

if(UNIX)
	add_definitions("-std=c++0x -fno-rtti")
endif()

include_directories(${CONAN_INCLUDE_DIRS})
add_executable(test test.cpp)
target_link_libraries(test ${CONAN_LIBS})
