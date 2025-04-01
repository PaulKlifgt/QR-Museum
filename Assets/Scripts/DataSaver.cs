using System;
using System.Collections.Generic;
using UnityEngine;

public class DataSaver : MonoBehaviour
{
    public static void SaveScanned(int id)
    {
        string scannedYet = PlayerPrefs.GetString("scannedID", "");
        PlayerPrefs.SetString("scannedID", scannedYet + id.ToString() + " ");

    }


    public static List<int> GetSaved()
    {

        string scannedIDs = PlayerPrefs.GetString("scannedID", "");
        string[] separatedIDs = scannedIDs.Split(' ');
        List<int> IDs = new List<int>();
        foreach (string ID in separatedIDs)
        {
            if (ID != "")
            {
                IDs.Add(int.Parse(ID));
            }
        }
        return IDs;
    }
}