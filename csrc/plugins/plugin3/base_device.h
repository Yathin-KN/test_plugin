#pragma once

class BaseDevice {
public:
    virtual void do_something() = 0;
    virtual ~BaseDevice() = default;
};
