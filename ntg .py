<h4>Pagination</h4>
<div class="row m-5">
    <div class="col-md-12 m3">
        {% if products.has_other_pages  %}
    <nav aria-label="...">

      <ul class="pagination">
      <!-- Here Previous Page stars here -->
          {% if products.has_previous %}
        <li class="page-item">
            <a href="?page={{ product.previous_page_number  }}" class="page-link">Previous</a>
        </li>
            {% else %}
        <li class="page-item disabled">
            <a href="?page={{ products.paginator.number_pages }}" class="page-link">Previous</a>
        </li>
       {% endif %}
    <!-- Here Previous page ends here -->

          <!-- Open Number paginator -->
          {% for i in products.paginator.page_range %}
          {% if products.number == i %}
            <li class="page-item active">
                <a class="page-link" href="?page={{ i }}">{{ i }}</a>
            </li>
          {% else %}
          <li class="page-item">
              <a class="page-link" href="?page={{ i }}" aria-current="page">{{i}}</a>
          </li>
          {% endif %}
          {% endfor %}
          <!-- closed Number paginator -->

          <!-- Here next Button is started -->
        {% if products.has_next %}
        <li class="page-item">
            <a class="page-link" href="?page={{ products.next_page_number }}">Next</a>
        </li>
          {% else %}
        <li class="page-item disabled">
            <a class="page-link" href="?page={{ products.paginator.number_pages }}">Next</a>
        </li>
        {% endif %}
          <!-- Here next Button is ends here -->
      </ul>
    </nav>
        {% endif %}
    </div>
 
