#include "plugin2.h"

extern "C" BaseDevice* create_device() {
    return new Plugin2();
}
