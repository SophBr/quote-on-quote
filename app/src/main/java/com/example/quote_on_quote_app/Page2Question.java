package com.example.quote_on_quote_app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class Page2Question extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.example.quote-on-quote_app.MESSAGE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_page2_question);
    }
}