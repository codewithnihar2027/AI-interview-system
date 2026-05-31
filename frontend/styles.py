def load_css():
    return """
    <style>

   .hero{
    text-align:center;
    padding:12px 20px;
    border-radius:18px;
    background:linear-gradient(
    135deg,
    #4F46E5,
    #7C3AED
    );
    color:white;
    margin-bottom:15px;
}

.hero h1{
    font-size:34px;
    margin-bottom:3px;
}

.hero p{
    font-size:15px;
    margin:0;
}
    .question-card{
        padding:20px;
        border-radius:15px;
        background:#1e293b;
        color:white;
        font-size:18px;
    }

    .feedback-card{
        padding:15px;
        border-radius:15px;
        background:#1e293b;
        min-height:220px;
    }

    div.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;

    background:linear-gradient(
        135deg,
        #4F46E5,
        #7C3AED
    );

    color:white;
    border:none;
    transition:0.3s;
}

div.stButton > button:hover{
    transform:scale(1.02);
    box-shadow:0 0 20px rgba(124,58,237,0.5);
}
    </style>
    """
