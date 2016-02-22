#include "fakeit.hpp"

using namespace fakeit;

struct SomeInterface {
    virtual int foo() = 0;
};

int main() {
    Mock<SomeInterface> mock;
    When(Method(mock, foo)).Return(0);
    SomeInterface &i = mock.get();
    return i.foo();
}
