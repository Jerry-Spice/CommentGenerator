#include <stdio.h>
#include <stdlib.h>

void say_how_are_you() {
    printf("How are you?");
}


struct coolstuff {
    int name;
};

int main(int argc, char* argv[]) {

    printf("Hello World!\n");
    say_how_are_you();

    return 0;
}
