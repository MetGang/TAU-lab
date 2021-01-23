#define CATCH_CONFIG_MAIN // Catch2 tworzy funkcję main za nas
#include "catch.hpp"

int Factorial(int number)
{
    return number > 1 ? Factorial(number - 1) * number : 1;
}

TEST_CASE( "Silnia", "[Factorial]" )
{
    REQUIRE( Factorial(0) == 1 );
    REQUIRE( Factorial(1) == 1 );
    REQUIRE( Factorial(2) == 2 );
    REQUIRE( Factorial(3) == 6 );
    REQUIRE( Factorial(10) == 3628800 );
}

TEST_CASE( "Zmiana rozmiaru std::vector testując z TEST_CASE", "[std::vector]" )
{
    std::vector<int> v = { 0, 1, 2, 3, 4, 5 };

    REQUIRE( v.size() == 6 );
    REQUIRE( v.capacity() == 6 );

    SECTION( "Powiększenie rozmiaru zmienia rozmiar oraz pojemność" )
    {
        v.resize( 10 );

        REQUIRE( v.size() == 10 );
        REQUIRE( v.capacity() >= 10 );
    }

    SECTION( "Zmniejszenie rozmiaru zmienia rozmiar, ale nie pojemność" )
    {
        v.resize( 0 );

        REQUIRE( v.size() == 0 );
        REQUIRE( v.capacity() >= 6 );
    }

    SECTION( "Rezerwowanie większego rozmiaru zwiększa pojemność, ale nie rozmiar" )
    {
        v.reserve( 10 );

        REQUIRE( v.size() == 6 );
        REQUIRE( v.capacity() >= 10 );
    }

    SECTION( "Rezerwowanie mniejszego rozmiaru nie wpływa na std::vector" )
    {
        v.reserve( 0 );

        REQUIRE( v.size() == 6 );
        REQUIRE( v.capacity() >= 6 );
    }
}

SCENARIO( "Zmiana rozmiaru std::vector testując z SCENARIO", "[std::vector]" )
{
    GIVEN( "std::vector z 6 numerami" )
    {
        std::vector<int> v = { 0, 1, 2, 3, 4, 5 };

        REQUIRE( v.size() == 6 );
        REQUIRE( v.capacity() >= 6 );

        WHEN( "Zwiększenie rozmiaru" )
        {
            v.resize( 10 );

            THEN( "Rozmiar i pojemność się zwiększają" )
            {
                REQUIRE( v.size() == 10 );
                REQUIRE( v.capacity() >= 10 );
            }
        }

        WHEN( "Zmniejszenie rozmiaru" )
        {
            v.resize( 0 );

            THEN( "Rozmiar się zmniejsza, ale nie pojemość" )
            {
                REQUIRE( v.size() == 0 );
                REQUIRE( v.capacity() >= 6 );
            }
        }

        WHEN( "Rezerwowanie większego rozmaru" )
        {
            v.reserve( 10 );

            THEN( "Pojemność się zwiększa, ale nie rozmiar" )
            {
                REQUIRE( v.size() == 6 );
                REQUIRE( v.capacity() >= 10 );
            }
        }

        WHEN( "Rezerwowanie mniejszego rozmaru" )
        {
            v.reserve( 0 );

            THEN( "Rozmiar i pojemność bez zmian" )
            {
                REQUIRE( v.size() == 6 );
                REQUIRE( v.capacity() >= 6 );
            }
        }
    }
}

TEST_CASE( "Pusty test, który kończy się sukcesem", "[compilation-only]")
{
    SUCCEED( "Działa!" );
}

TEST_CASE( "Testowanie losowych liczb całkowitych w zakresie", "[generator]" )
{
    SECTION( "50 liczb całkowitych w zakresie [-100, 100]" )
    {
        auto i = GENERATE(take(50, random(-100, 100)));

        REQUIRE( i >= -100 );
        REQUIRE( i <= 100 );
    }

    SECTION( "100 liczb całkowitych w zakresie [-1000, 1000]" )
    {
        auto i = GENERATE(take(100, random(-1000, 1000)));

        REQUIRE( i >= -1000 );
        REQUIRE( i <= 1000 );
    }
}

TEST_CASE( "Testowanie wyrzucania wyjątków", "[exception]" )
{
    CHECK_THROWS(throw nullptr);
}
