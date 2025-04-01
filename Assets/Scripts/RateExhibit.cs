using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using UnityEngine;
using UnityEngine.UI;


public class RateExhibit : MonoBehaviour
{
    [SerializeField]
    private Sprite starOn;
    [SerializeField]
    private Sprite starOff;
    [SerializeField]
    private Image[] rateButtons;
    [SerializeField]
    private PopUp popup;
    public void SetRate(int rate)
    {

        for (int i = 0; i < 5; i++)
        {
            if (i < rate)
            {
                rateButtons[i].sprite = starOn;
            }
            else
            {
                rateButtons[i].sprite = starOff;
            }
            
        }
        if (rate != 0 && !DataSaver.GetRated().Contains(popup.lastScan))
        {
            SendRate(popup.lastScan, rate);
        }
    }
    public void SendRate(int id, int rate)
    {
        var client = new HttpClient();
        client.BaseAddress = new System.Uri("https://qrmuseum.tw1.ru/");
        var response = client.GetAsync("api/rank/" + id + "/" + rate).Result;

        var respons = client.GetAsync("api/exh/" + id).Result;
        string responseContent = respons.Content.ReadAsStringAsync().Result;
        var exhibit = SimpleJSON.JSON.Parse(responseContent);
        popup.UpdateRate(exhibit[2]);
        DataSaver.SaveRated(id);
    }
}
