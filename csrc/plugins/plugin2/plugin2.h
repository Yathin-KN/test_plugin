#pragma once

#include <iostream>
#include "base_device.h"

class Plugin2 : public BaseDevice {
public:
    void do_something() override {
        std::cout << "Plugin2 doing something" << std::endl;
    }
};
