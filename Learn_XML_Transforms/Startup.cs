using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(Learn_XML_Transforms.Startup))]
namespace Learn_XML_Transforms
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}
