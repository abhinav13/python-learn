using NUnit.Framework;
using CalculatingDevices;
using sharenamespace;


namespace Calculator.Tests
{
    [TestFixture]
    public class CalculatorTests
    {
        [Test]
        public void ShouldAddTwoNumbers()
        {
            var sut = new CalculatingDevices.Calculator();
            var result = sut.Add(1, 2);
            var sut2 = new MyClass();
            sut2.PrintThis("blah");
            Assert.That(result, Is.EqualTo(4));

        }
    }
}
