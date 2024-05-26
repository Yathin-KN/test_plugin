#pragma once

#include <iostream>
#include "base_device.h"

class Plugin1 : public BaseDevice {
public:
    void do_something() override {
        std::cout << "Plugin1 doing something" << std::endl;
    }
};
