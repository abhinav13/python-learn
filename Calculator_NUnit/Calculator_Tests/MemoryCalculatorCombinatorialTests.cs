using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CalculatingDevices;
using NUnit.Core;
using NUnit.Framework;

namespace Calculator_Tests
{
    [TestFixture]
    public  class MemoryCalculatorCombinatorialTests
    {
        [Test]
        public void ShouldAddAndDivide([Values(10, 20, 30)] int numToAdd,
            [Values(10, 2, 1)] int numToDivideBy)
        {
            var sut = new Calculator();
            sut.RememberAdd(numToAdd);
            sut.DivideBy(numToDivideBy);
        }

    }
}
