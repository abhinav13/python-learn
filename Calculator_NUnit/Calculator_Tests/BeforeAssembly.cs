using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NUnit.Core;
using NUnit.Framework;

[SetUpFixture]
public class BeforeAssembly
{

    [SetUp]
    public void RunBeforeAnyTestsinNameSpace()
    {
	    Console.WriteLine("##### Before Any Tests in namespace");
    }

    [TearDown]
    public void RunAfterAnyTestsinNameSpace()
    {
        Console.WriteLine("### After all tests in SomeNameSpace");   
    }
}

