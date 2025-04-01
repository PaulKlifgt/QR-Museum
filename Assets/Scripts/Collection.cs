using System.Net.Http;
using UnityEngine;
using System.Collections.Generic;

public class Collection : MonoBehaviour
{
    [SerializeField]
    private GameObject exhibitPrefab;
    [SerializeField]
    private Transform content;

    public void OnEnable()
    {
        foreach (Transform contentChild in content)
        {
            Destroy(contentChild.gameObject);
        }
        var client = new HttpClient();
        client.BaseAddress = new System.Uri("http://127.0.0.1:8000/");
        var response = client.GetAsync("api/all_sec").Result;


        if (response.IsSuccessStatusCode)
        {
            string responseContent = response.Content.ReadAsStringAsync().Result; //return JSon-string 
            Debug.Log(responseContent);
            var sections = SimpleJSON.JSON.Parse(responseContent);
            for (int i = 0; i < sections.Count; i++)
            {
                for (int j = 0; j < sections[i].Count; j++)
                {
                    bool isScanned = false;
                    GameObject spawnedExhibit = Instantiate(exhibitPrefab, content);
                    ExhibitFrame exhibitFrame = spawnedExhibit.GetComponent<ExhibitFrame>();
                    if (DataSaver.GetSaved().Contains(sections[i][j][0]))
                    {
                        isScanned = true;
                    }
                    exhibitFrame.SetData(null, sections[i][j][1], sections[i][j][3], isScanned);
                }
            }
        }
        
    }
}


public class Exhibit
{
    public int id;
    public string name;
    public string description;
    public float average_rank;
    public int count_rank;
}


public class Exhibits
{
    public List<Exhibit> exhibits;
}