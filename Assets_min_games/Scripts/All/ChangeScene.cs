using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ChangeScene : MonoBehaviour
{
    public void Again()
    {
        UnityEngine.SceneManagement.SceneManager.LoadScene(UnityEngine.SceneManagement.SceneManager.GetActiveScene().buildIndex);
    }
    public void LoadScenes()
    {
        SceneManager.LoadScene("Main", LoadSceneMode.Additive);
    }
    // public void ChangeScene(string sceneName)
    // {
    //     UnityEngine.SceneManagement.SceneManager.LoadScene(name);
    // }
    // public void Exit()
    // {
    //     Application.Quit();
    // }
}
