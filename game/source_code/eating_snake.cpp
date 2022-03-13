#include <random>
#include <array>
#include <string>
#include <map>
#include <ctime>
using namespace std;

class Food
{
    static default_random_engine e;
    unsigned height;
    unsigned widge;
    char kind;
    int x;
    int y;
    uniform_int_distribution<unsigned> u_x(0, widge);
    uniform_int_distribution<unsigned> u_y(0, widge);
public:
    Food(unsigned h, unsigned w, char k):
        height(h), widge(w), kind(k){*this.food_xy()}
    Food() = delete;
    ~Food() = default;
    void food_xy();
};

void Food::food_xy(){
    *this.e.seed(time(nullptr));
    *this.x = u_x(e);
    *this.y = u_x(e);
    return;
}

class Snake
{
    char head_kind;
    char tail_kind;
    unsigned point = 0;
    unsigned x = 0;
    unsigned y = 0;
    map<char, vector<unsigned>> xy_dic{'x':{0}, 'y':{0}};
public:
    Snake(const char& hk, const char& tk){}
    ~Snake();
    
};

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}