package com.example.streamlitwrapper1275iso

import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import com.example.streamlitwrapper1275iso.ui.theme.StreamlitWrapper1275ISOTheme
import androidx.core.view.WindowCompat

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        WindowCompat.setDecorFitsSystemWindows(window, false)  // Add this line
        setContent {
            StreamlitWrapper1275ISOTheme {
                // Remove the Box with systemBarsPadding for now to ensure the WebView gets full screen
                AndroidView(
                    modifier = Modifier.fillMaxSize(),
                    factory = { context ->
                        WebView(context).apply {
                            settings.javaScriptEnabled = true
                            settings.domStorageEnabled = true

                            // These settings help the page scale properly:
                             settings.useWideViewPort = true
                             settings.loadWithOverviewMode = true

                            // Force a mobile user agent so that the page is served in mobile mode:
                            settings.userAgentString = "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36"

                            webViewClient = WebViewClient()
                            loadUrl("https://1275vsiso-mqhmnvbwhnptp8dacpt5a5.streamlit.app/")
                        }
                    }
                )
            }
        }
    }
}
