#ifndef GAMEOBJECT_H
#define GAMEOBJECT_H

class GameObject {
public:
    GameObject();
    ~GameObject();
    void update();
    void render();
private:
    int x, y;
};

#endif // GAMEOBJECT_H
