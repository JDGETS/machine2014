using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;

namespace machine2014arcade.Game
{
    [Serializable]
    class ScoreCard : ISerializable
    {
        public String Photo { get; set; }
        public String University;
        public int Score;

        public ScoreCard()
        {

        }

        // Serialization needed
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.AddValue("Score", Score, typeof(int));
            info.AddValue("Photo", Photo, typeof(string));
            info.AddValue("University", University, typeof(string));

        }

        //Deserialization needed
        public ScoreCard(SerializationInfo info, StreamingContext context)
        {
            // Reset the property value using the GetValue method.
            Score = (int)info.GetValue("Score", typeof(int));
            Photo = (string)info.GetValue("Photo", typeof(string));
            University = (string)info.GetValue("University", typeof(string));
        }

        public void save(string filename)
        {
            FileStream stream = new FileStream(filename, FileMode.Create);
            IFormatter formatter = new BinaryFormatter();
            formatter.Serialize(stream, this);
            stream.Close();
        }

        public static ScoreCard load(string filename)
        {
            ScoreCard card = null;
            FileStream stream = new FileStream(filename, FileMode.Open);
            IFormatter formatter = new BinaryFormatter();
            card = (ScoreCard)formatter.Deserialize(stream);
            stream.Close();

            return card;
        }
    }
}
