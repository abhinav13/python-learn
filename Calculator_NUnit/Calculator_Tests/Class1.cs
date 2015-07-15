using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Runtime;
using System.Text;
using System.Threading.Tasks;
using NUnit.Framework;
using CalculatingDevices;

namespace Calculator_Tests
{

    [TestFixture]
    [Category("AllTests")]
    public class SimpleCalculatorTests
    {
        [SetUp]
        public void SetupTests()
        {
            Console.WriteLine("Before running Test {0}", TestContext.CurrentContext.Test.Name);
        }

        [TearDown]
        public void TestTearDown()
        {
            Console.WriteLine("After running Test {0}", TestContext.CurrentContext.Test.Name);
        }

        [Test]
        public void ShouldAddTwoNumbers()
        {
            var sut = new Calculator();
            var result = sut.Add(1, 2);
            Assert.That(result,Is.EqualTo(3));
        }

        [Test]
        [Category("Multiply")]
        public void ShouldMultiplyTwoNumbers()
        {
            var sut = new Calculator();
            var result = sut.Multiply(2,10);
            Assert.That(result, Is.EqualTo(20));
        }

        [Test]
        public void ShouldIncreaseNumbers()
        {
            var sut = new Calculator();
            var result = sut.IncreaseRandomAmount(100);
            Assert.That(result, Is.GreaterThan(100));
        }

        [Test]
        //using doubles to showcase Is.Equal with a fault taulrance of 0.1
        
        public void ShouldAddDouble()
        {
            var sut = new Calculator();
            var result = sut.AddDouble(2.33, 3.77);
            Assert.That(result,Is.EqualTo(6.00).Within(0.1));
        }

        [Test]
        //using doubles to showcase Is.Equal with a fault taulrance of 0.1

        public void ShouldAddDoublewithFaultPercentage()
        {
            var sut = new Calculator();
            var result = sut.AddDouble(2.33, 3.77);
            Assert.That(result, Is.EqualTo(6.00).Within(1.7).Percent);
        }

        [Test]
        //The list should not be empty

        public void ShouldNotallowEmptyList()
        {
            var sut = new Calculator();
            var result = sut.ButtonList();
            Assert.That(result, Is.Not.Empty);
        }

        [Test]
        public void ShouldNotAllowEmptyEntriesinList()
        {
            var sut = new Calculator();
            var result = sut.EmptyItemsInButtonList();
            Assert.That(result, Is.All.Not.Empty);
        }

        [Test]
        //This check if there is only 1 unique item in a list
        public void ShouldOnlyContainOneButton()
        {
            var sut = new Calculator();
            var result = sut.ButtonList();
            Assert.That(result, Has.Exactly(1).Contains("One").IgnoreCase);
        }
        [Test]
        public void ShouldContainUniqueButtons()
        {
            var sut = new Calculator();
            var result = sut.ButtonList();
            Assert.That(result, Is.Unique);
        }

        [Test]
        public void ShouldThrow_ExplicitExceptionDivideByZero()
        {
            var sut = new Calculator();
            Assert.That(()=>{throw new ArgumentOutOfRangeException();}, Throws.TypeOf<ArgumentOutOfRangeException>());
        }

        [Test]
        public void ShouldErrorWhenDivideByZero()
        {
            var sut = new Calculator();
            Assert.That(() => sut.DividbyZero(1,0),Throws.Exception);
        }

        [Test]
        public void ShouldThrow_ExplicitExceptionWithParam()
        {
            var sut = new Calculator();
            Assert.That(()=>sut.DivideByZeroThrowException(200,100),Throws.InstanceOf<ArgumentOutOfRangeException>()
                            .With.Matches<ArgumentOutOfRangeException>(x=>x.ParamName=="value"));
        }

        
        [TestCaseSource(typeof(ExampleTestCaseSource))]
        public void ShouldSubtractTwoNegativeNumbers(int firstnum, int secondnum, int expectednum)
        {
            var sut = new Calculator();
            sut.RememberSubtract(firstnum);
            sut.RememberSubtract(secondnum);
            Assert.That(sut.Value, Is.EqualTo(expectednum));
        }

        //THis test is ignored due to the ignore attribute
        [Test]
        [Ignore]
        public void ShouldIgnoreTest([Values(2)] int num)
        {
            var sut = new Calculator();
            var result = sut.Multiply(2, 3);
            Assert.That(result, Is.EqualTo(6));
        }

        [Test]
        [Category("Multiply")]
        public void ShouldMultipleCategory([Values(2)] int num)
        {
            var sut = new Calculator();
            var result = sut.Multiply(2, 3);
            Assert.That(result, Is.EqualTo(6));
        }

        [Test]
        [MaxTime(5500)]
        public void ShouldTakeSpecificTime()
        {
            var sut = new Calculator();
            Assert.That(()=>sut.TakesLongTime(2),Is.EqualTo(2));
        }

        //THis test will repeat each time 10000 times with each input.
        //This is used for debugging.
        [Test]
        [Repeat(10000)]
        public void ShouldTestRandomFailures([Values(100,1000,10001)]int a)
        {
            var sut = new Calculator();
            Assert.That(()=>sut.FailRandomly(a),Is.EqualTo(a));
        }
    }

    public class ExampleTestCaseSource : IEnumerable
    {

        public IEnumerator GetEnumerator()
        {
            yield return new[] {-5, -10, 15};
            yield return new[] {-5, -5, 10};
            yield return new[] {-5, 0, 5};
        }
    }

    //This a test that will be ignored due to the ignore attribute
    
}
