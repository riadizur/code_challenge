#ifndef GRAPHICSMANAGER_H
#define GRAPHICSMANAGER_H

#include <vector>
#include "GameObject.h"

class GraphicsManager {
public:
    GraphicsManager();
    ~GraphicsManager();
    void init();
    void render(const std::vector<GameObject>& gameObjects);
};

#endif // GRAPHICSMANAGER_H
