package com.example.streamlitwrapper1275iso

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.streamlitwrapper1275iso.ui.theme.StreamlitWrapper1275ISOTheme
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.viewinterop.AndroidView
import android.webkit.WebView
import android.webkit.WebViewClient



class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            StreamlitWrapper1275ISOTheme {
                AndroidView(
                    modifier = Modifier.fillMaxSize(),
                    factory = { context ->
                        WebView(context).apply {
                            // Enable JavaScript and DOM storage
                            settings.javaScriptEnabled = true
                            settings.domStorageEnabled = true



                            // Tell the WebView to use a wide viewport and load pages in overview mode
                            settings.useWideViewPort = true
                            settings.loadWithOverviewMode = true

                            // Optionally enable zoom controls if needed
                            settings.setSupportZoom(true)
                            settings.builtInZoomControls = true
                            settings.displayZoomControls = false

                            webViewClient = WebViewClient()
                            loadUrl("https://1275vsiso-mqhmnvbwhnptp8dacpt5a5.streamlit.app/")
                        }
                    }
                )

            }
        }
    }
}




@Composable
fun StreamlitWebView(url: String, modifier: Modifier = Modifier) {
    AndroidView(
        modifier = modifier.fillMaxSize(),
        factory = { context ->
            WebView(context).apply {
                settings.javaScriptEnabled = true  // Enable JS if your Streamlit page needs it
                webViewClient = WebViewClient()     // Keep navigation inside the WebView
                loadUrl(url)                       // Load your Streamlit URL
            }
        }
    )
}

