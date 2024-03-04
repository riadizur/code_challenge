#include "Game.h"
#include <iostream>
#include <thread> // For delaying

Game::Game() : isRunning(true) {}

Game::~Game() {}

void Game::init() {
    // Initialize game objects, setup scene, etc.
    // For simplicity, let's just create a single game object for demonstration
    gameObjects.push_back(GameObject());
}

void Game::run() {
    while (isRunning) {
        // Update game objects, physics, collision detection, etc.
        for (auto& gameObject : gameObjects) {
            gameObject.update();
        }

        // Render game objects
        for (auto& gameObject : gameObjects) {
            gameObject.render();
        }

        // Add a delay to control frame rate
        std::this_thread::sleep_for(std::chrono::milliseconds(16)); // Aim for approximately 60 FPS
    }
}
