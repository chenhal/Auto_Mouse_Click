#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <windows.h>
using namespace std;
int main()
{
    cout << "Welcome to Auto_Mouse_Click!! By DylanC" << endl;
    cout << "\n";
    cout << "Please prees 'Space' to get your x_coordinate && y_coordinate after you move you mouse where you want to click!! " << endl;
    int x, y;
    int num;
    while (1)
    {
        if (GetAsyncKeyState(VK_SPACE))
        {
            while (1)
            {
                POINT p;
                GetCursorPos(&p);
                cout << "(x,y) : " << p.x << "," << p.y << endl;
                break;
            }
            cout << "Input your x_coordinate: ";
            cin >> x;
            cout << "\n";
            cout << "Input your y_coordinate: ";
            cin >> y;
            cout << "\n";
            cout << "The number of click (No more than 100000 recommended): ";
            cin >> num;
            cout << "\n";
            cout << "Start!! ";
            system("pause");
            Sleep(1000);
            SetCursorPos(x, y);
            for (int i = 0; i < num; i++)
            {
                mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
                mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
            }
        }
    }
    return 0;
}
// Copyright by DylanC