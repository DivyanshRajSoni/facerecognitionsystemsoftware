#include<SFML/Graphics.hpp>
using namespace std;
int main() {
    sf::RenderWindow window(sf::VideoMode(800, 600), "Teddy Bear");

    // Create the teddy bear's body parts
    sf::CircleShape head(50);
    head.setFillColor(sf::Color(139, 69, 19)); // Brown color
    head.setPosition(375, 150);

    sf::CircleShape body(75);
    body.setFillColor(sf::Color(139, 69, 19));
    body.setPosition(350, 250);

    sf::CircleShape ear1(30);
    ear1.setFillColor(sf::Color(139, 69, 19));
    ear1.setPosition(320, 100);

    sf::CircleShape ear2(30);
    ear2.setFillColor(sf::Color(139, 69, 19));
    ear2.setPosition(450, 100);

    sf::CircleShape eye1(10);
    eye1.setFillColor(sf::Color::Black);
    eye1.setPosition(395, 180);

    sf::CircleShape eye2(10);
    eye2.setFillColor(sf::Color::Black);
    eye2.setPosition(445, 180);

    sf::CircleShape nose(8);
    nose.setFillColor(sf::Color::Black);
    nose.setPosition(423, 205);

    sf::ConvexShape mouth;
    mouth.setPointCount(3);
    mouth.setPoint(0, sf::Vector2f(420, 220));
    mouth.setPoint(1, sf::Vector2f(430, 220));
    mouth.setPoint(2, sf::Vector2f(425, 230));
    mouth.setFillColor(sf::Color::Black);

    sf::CircleShape arm1(25);
    arm1.setFillColor(sf::Color(139, 69, 19));
    arm1.setPosition(275, 300);

    sf::CircleShape arm2(25);
    arm2.setFillColor(sf::Color(139, 69, 19));
    arm2.setPosition(500, 300);

    sf::CircleShape leg1(35);
    leg1.setFillColor(sf::Color(139, 69, 19));
    leg1.setPosition(335, 400);

    sf::CircleShape leg2(35);
    leg2.setFillColor(sf::Color(139, 69, 19));
    leg2.setPosition(430, 400);

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear(sf::Color::White);
        window.draw(head);
        window.draw(body);
        window.draw(ear1);
        window.draw(ear2);
        window.draw(eye1);
        window.draw(eye2);
        window.draw(nose);
        window.draw(mouth);
        window.draw(arm1);
        window.draw(arm2);
        window.draw(leg1);
        window.draw(leg2);
        window.display();
    }

    return 0;
}
