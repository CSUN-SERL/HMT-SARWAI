using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Text;

namespace HmtRequest {
    internal class Program {
        public static void Main(string[] args) {

//            var post = Encoding.UTF8.GetBytes("{\"status\": false}");
            
            const string url = @"http://192.168.1.14:9999/query";
            var request = (HttpWebRequest) WebRequest.Create(url);
            request.Method = "Post";
            request.ContentType = "application/json; charset=UTF-8";
            request.Accept = "application/json";
//            request.ContentLength = post.Length;

//            var sendStream = request.GetRequestStream();
//            sendStream.Write(post, 0, post.Length);
//            sendStream.Close();

            var response = (HttpWebResponse) request.GetResponse();
            Console.WriteLine(response.ContentLength);
            Console.WriteLine(response.ContentType);

            var getStream = response.GetResponseStream();
            StreamReader readStream = null;
            if (getStream != null)
                readStream = new StreamReader(getStream, Encoding.UTF8);

            if (readStream != null) {
                Console.WriteLine(readStream.ReadToEnd());
                readStream.Close();
            }
            
            response.Close();
        }
    }
}