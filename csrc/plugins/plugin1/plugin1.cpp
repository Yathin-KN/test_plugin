#include "plugin1.h"

extern "C" BaseDevice* create_device() {
    return new Plugin1();
}
