#include "plugin3.h"

extern "C" BaseDevice* create_device() {
    return new Plugin3();
}
