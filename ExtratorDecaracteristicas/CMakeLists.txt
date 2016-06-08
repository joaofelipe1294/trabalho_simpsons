
cmake_minimum_required(VERSION 2.8)
 
project(ExtratorDeCaracteristicas)
 
find_package(ITK REQUIRED)
include(${ITK_USE_FILE})
 
add_executable(ExtratorDeCaracteristicas main.cpp)
target_link_libraries(ExtratorDeCaracteristicas ${ITK_LIBRARIES})
