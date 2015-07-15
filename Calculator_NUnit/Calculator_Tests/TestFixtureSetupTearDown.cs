using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NUnit.Framework;

namespace Calculator_Tests
{
    [SetUpFixture]
    class TestFixtureSetupTearDown
    {

        [SetUp]
        public void BeforeTestsRun()
        {
            Console.WriteLine("Before TestFixture Setup", TestContext.CurrentContext.Test);
        }

        [TearDown]
        public void AfterTearDown()
        {
            Console.WriteLine("After TestFixture Setup", TestContext.CurrentContext.Test);
        }
    }
}
