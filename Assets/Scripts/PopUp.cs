using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using UnityEngine;
using TMPro;

public class PopUp : MonoBehaviour
{
    [SerializeField]
    private Animator animator;
    [SerializeField]
    private QRScanner qr;
    [SerializeField]
    private TMP_Text name;
    [SerializeField]
    private TMP_Text description;
    [SerializeField]
    private TMP_Text star;
    [SerializeField]
    private TMP_Text star2;
    [SerializeField]
    private string starSymbol;
    [SerializeField]
    private GameObject rateButton;
    public int lastScan;
    [SerializeField]
    private GameObject rateYet;
    [SerializeField]
    private GameObject notRateYet;

    public void Show(int id)
    {
        rateButton.SetActive(true);
        animator.SetBool("isOpen", true);
        var client = new HttpClient();
        client.BaseAddress = new System.Uri("https://qrmuseum.tw1.ru/");
        var response = client.GetAsync("api/exh/" + id).Result;
        string responseContent = response.Content.ReadAsStringAsync().Result;
        Debug.Log(responseContent);
        var exhibit = SimpleJSON.JSON.Parse(responseContent);
        name.text = exhibit[0];
        description.text = exhibit[1];
        star.text = exhibit[2] + starSymbol;
        star2.text = exhibit[2] + starSymbol;
        lastScan = id;
        if (!DataSaver.GetRated().Contains(id))
        {
            notRateYet.SetActive(true);
            rateYet.SetActive(false);
        }
        else
        {
            notRateYet.SetActive(false);
            rateYet.SetActive(true);
        }
    }


    public void UpdateRate(float rate)
    {
        star.text = rate.ToString() + starSymbol;
        star2.text = rate.ToString() + starSymbol;
    }
}
