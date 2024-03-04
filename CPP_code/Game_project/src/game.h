#ifndef GAME_H
#define GAME_H

#include "GraphicsManager.h"
#include "InputManager.h"
#include "ResourceManager.h"
#include "GameObject.h"
#include <vector>

class Game {
public:
    Game();
    ~Game();
    void init();
    void run();
private:
    GraphicsManager graphicsManager;
    InputManager inputManager;
    ResourceManager resourceManager;
    std::vector<GameObject> gameObjects;
    bool isRunning;
};

#endif // GAME_H
