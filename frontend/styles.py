def load_css():
    return """
    <style>

    .hero{
        text-align:center;
        padding:30px;
        border-radius:20px;
        background:linear-gradient(
        135deg,
        #4F46E5,
        #7C3AED
        );
        color:white;
        margin-bottom:30px;
    }

    .hero h1{
        font-size:48px;
        margin-bottom:10px;
    }

    .hero p{
        font-size:20px;
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
    }

    </style>
    """