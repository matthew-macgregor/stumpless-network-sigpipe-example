cmake_minimum_required(VERSION 3.10)

# set the project name
project(network-example C)

# add the executable
add_executable(network-example src/network_example.c)

option(IGNORE_SIGPIPE "Ignore SIGPIPE Signal" OFF)
if(IGNORE_SIGPIPE)
    add_definitions(-DIGNORE_SIGPIPE)
elseif(HANDLE_SIGPIPE)
    add_definitions(-DHANDLE_SIGPIPE)
endif()

target_link_libraries(network-example PUBLIC stumpless)

set_property(TARGET network-example PROPERTY C_STANDARD 11)
