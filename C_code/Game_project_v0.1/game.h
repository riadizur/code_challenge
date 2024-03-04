#ifndef GAME_H
#define GAME_H

#include <vector>
#include "GameObject.h"

class Game {
public:
    Game();
    ~Game();
    void init();
    void run();
private:
    std::vector<GameObject> gameObjects;
    bool isRunning;
};

#endif // GAME_H
