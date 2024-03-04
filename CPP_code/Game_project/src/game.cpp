#include "Game.h"

Game::Game() : isRunning(true) {}

Game::~Game() {}

void Game::init() {
    graphicsManager.init();
    inputManager.init();
    resourceManager.loadAllResources(); // Load game assets
    // Initialize game objects, setup scene, etc.
}

void Game::run() {
    while (isRunning) {
        inputManager.processInput();
        // Update game objects, physics, collision detection, etc.
        // Render game objects
        graphicsManager.render(gameObjects);
    }
}
