#include "GameObject.h"
#include <iostream>

GameObject::GameObject() : x(100), y(100) {}

GameObject::~GameObject() {}

void GameObject::update() {
    // Update game object state
    // For simplicity, let's just move the object horizontally
    x += 1;
}

void GameObject::render() {
    // Render object
    // For now, we'll just output its position to the console
    std::cout << "Object Position: (" << x << ", " << y << ")" << std::endl;
}
