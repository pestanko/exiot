cmake_minimum_required(VERSION 3.0)
project(mini_not_implemented)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_EXTENSIONS OFF)

if (CMAKE_CXX_COMPILER_ID MATCHES Clang OR ${CMAKE_CXX_COMPILER_ID} STREQUAL GNU)
  # using regular Clang or AppleClang or GCC
  set(CMAKE_C_FLAGS "-pedantic -Wall -Wextra -Werror -g -Og")
elseif (${CMAKE_CXX_COMPILER_ID} STREQUAL MSVC)
  # using Visual Studio C++
  set(CMAKE_CXX_FLAGS "/permissive- /W4 /EHsc")
  add_definitions("-D_CRT_SECURE_NO_WARNINGS")
endif()

file(GLOB   SUBDIRS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} task*)

foreach(TASK ${SUBDIRS})
    if(IS_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/${TASK}")
        add_subdirectory(${TASK})
    endif()
endforeach()
