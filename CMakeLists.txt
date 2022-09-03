cmake_minimum_required(VERSION 3.10)

# set the project name
project(network-example C)

# add the executable
add_executable(network-example src/network_example.c)

option(HANDLE_SIGPIPE "Handle SIGPIPE Signal" OFF)
if( HANDLE_SIGPIPE )
    add_definitions(-DHANDLE_SIGPIPE)
endif()


target_link_libraries(network-example PUBLIC stumpless)

set_property(TARGET network-example PROPERTY C_STANDARD 11)

