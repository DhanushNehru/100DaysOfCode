using System;
using System.Xml;
using System.IO;
using Spire.Doc;
using System.Collections;

namespace C_
{
  class Program
  {
    static void Main(string[] args)
    {

      // This is to convert to xml doc
      Document doc = new Document();
      doc.LoadFromFile("Sample.html");
      doc.SaveToFile("Sample.xml", FileFormat.Xml);

      // XmlDataDocument xmldoc = new XmlDataDocument();
      // XmlNodeList xmlnode;
      // xmlnode = xmldoc.GetElementsByTagName("text");
    }
  }
}