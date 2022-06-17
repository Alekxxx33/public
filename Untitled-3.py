<!-- todo/templates/zadania_lista.html -->
<html>
<title>{config.SITE_NAME}_ </title>

<head>
    <title>
        {{config.SITE_NAME}}
    </title>
    <link rel="stylesheet" type=""text/css"
href="{{url-for('static'filename='style.css')}}">
</head>
<body>
    <h1>{{config.SITE_NAME}}</h1>

<ol>
    {{% for zadanie in zadania %}}
    <li>{{zaanie.zadanie}
 -<em> {{ zadanie.data_pub}}</em></li>
 {% endfor%}
<ol>
    % for zadanie in zadania %} <li>
        {% if zadanie.zrobione %}
        <span class-"done">{{zadanie.zadanie}}-<em>{{zadanie.data_pub}}</em>
        
        </span>
        { % else %}
        {{zadanie.zadanie}} -<em>{{zadanie.data_pub}}</em>
       { % endif %}
       {% if not zadanie.zrobione%}
<form method="POST" action=""{{url_for('zrobione')}">
<input type="hidden" name="id" value="{{zadanie.id}}"/>
<button type="submit">Wykonane</button>
</button>

</form>"
{% endif %}
    </li>
{% end for %}
</ol>
 
</ol>
</body>
</html>
