#pragma once

#include <iostream>
#include "base_device.h"

class Plugin3 : public BaseDevice {
public:
    void do_something() override {
        std::cout << "Plugin3 doing something" << std::endl;
    }
};
