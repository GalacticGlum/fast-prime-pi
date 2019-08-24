macro(CONFIG_NAME var)
    set(${var} $<$<CONFIG:Debug>:Debug>$<$<CONFIG:Release>:Release>)
endmacro(CONFIG_NAME)

CONFIG_NAME(_config)
cmake_minimum_required(VERSION 3.6)

# Setup the base project
# PPiCCG = Prime Pi convergence graph generator...
project(PPiCCG)

SET(PPiCCG_CMAKE_DIR "${PPiCCG_SOURCE_DIR}/CMake")
SET(PPiCCG_DEPEND_DIR "${PPiCCG_SOURCE_DIR}/Dependencies")

# add the -c and -Wall flags
if(MSVC)
	add_definitions(
		-c
	)
else()
	add_definitions(
		-c
		-Wall
	)
endif()

# defines
add_definitions( -D_CRT_SECURE_NO_WARNINGS )

# Lets load up our headers for the engine project
file(GLOB_RECURSE HDRS
	${PPiCCG_SOURCE_DIR}/Source/*.h
)

# Lets load up our sources for the engine project
file(GLOB_RECURSE SRCS
	${PPiCCG_SOURCE_DIR}/Source/*.cpp
	${PPiCCG_SOURCE_DIR}/Source/*.c
)

include_directories(${PPiCCG_SOURCE_DIR}/Source/Public)

# Define the executable
add_executable(PPiCCG ${HDRS} ${SRCS})
set_property(TARGET PPiCCG PROPERTY CXX_STANDARD 17)
set_property(TARGET PPiCCG PROPERTY CXX_STANDARD_REQUIRED ON)
set_target_properties(PPiCCG PROPERTIES LINKER_LANGUAGE CXX)

# Set the output directory for sandbox to make managing directories easier
set (PPiCCG_OUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/bin")
set_target_properties( PPiCCG PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PPiCCG_OUT_DIR})

target_compile_definitions(PPiCCG PUBLIC 
	"$<$<CONFIG:Release>:O2>" 
	"$<$<CONFIG:Release>:NDEBUG>"
)

target_compile_options(PPiCCG PUBLIC
	"$<$<CONFIG:Release>:-w>"
	"$<$<CONFIG:Debug>:-W4>"
)

# Primecount library
INCLUDE(${PPiCCG_CMAKE_DIR}/FindPrimecount.cmake)

# Define the include DIRs
include_directories(
    ${PPiCCG_SOURCE_DIR}/Source/Public
    ${Primecount_INCLUDE_DIRS}
)

# Define the link libraries
target_link_libraries( PPiCCG
	${Primecount_LIBRARIES}
)

# Copy binaries to output directory...
# Find all dependencies that have a bin folder...
include(${PPiCCG_CMAKE_DIR}/utils.cmake)
SUBDIRLIST(DEPENDENCY_DIRS ${PPiCCG_DEPEND_DIR})
foreach(dependency_name ${DEPENDENCY_DIRS})
	# check if there is a bin directory
	if(EXISTS "${PPiCCG_DEPEND_DIR}/${dependency_name}/bin")
		# there is a bin directory which means that we should copy this dependency
		add_custom_command(TARGET PPiCCG PRE_BUILD
						   COMMAND ${CMAKE_COMMAND} -E copy_directory
						   "${PPiCCG_DEPEND_DIR}/${dependency_name}/bin/${_config}/$<$<EQUAL:4,${CMAKE_SIZEOF_VOID_P}>:Win32>$<$<EQUAL:8,${CMAKE_SIZEOF_VOID_P}>:x64>" $<TARGET_FILE_DIR:PPiCCG>)
	endif()
endforeach()

# Set the working directory
file( WRITE "${CMAKE_CURRENT_BINARY_DIR}/PPiCCG.vcxproj.user" 
    "<?xml version=\"1.0\" encoding=\"utf-8\"?>     \
    <Project ToolsVersion=\"4.0\" xmlns=\"http://schemas.microsoft.com/developer/msbuild/2003\">
    <PropertyGroup Condition=\"'$(Configuration)|$(Platform)'=='Debug|x64'\">
        <LocalDebuggerWorkingDirectory>$(OutDir)</LocalDebuggerWorkingDirectory>
        <DebuggerFlavor>WindowsLocalDebugger</DebuggerFlavor>
    </PropertyGroup>
    <PropertyGroup Condition=\"'$(Configuration)|$(Platform)'=='Release|x64'\">
        <LocalDebuggerWorkingDirectory>$(OutDir)</LocalDebuggerWorkingDirectory>
        <DebuggerFlavor>WindowsLocalDebugger</DebuggerFlavor>
    </PropertyGroup>
	</Project>"
)

# Create virtual folders to make it look nicer in VS
if(MSVC_IDE)
	foreach(source IN LISTS SRCS HDRS)
		get_filename_component(source_path "${source}" PATH)
		string(REPLACE "${PPiCCG_SOURCE_DIR}" "" relative_source_path "${source_path}")
		string(REPLACE "/" "\\" source_path_msvc "${relative_source_path}")
		string(REPLACE "Source\\" "" actual_source_path_msvc "${source_path_msvc}")
		source_group("${actual_source_path_msvc}" FILES "${source}")
	endforeach()
endif()

if (MSVC)
    set_property(DIRECTORY PROPERTY VS_STARTUP_PROJECT PPiCCG)
endif (MSVC)