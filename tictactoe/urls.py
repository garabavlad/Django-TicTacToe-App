"""
Examples:
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from .views import welcome as home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^player/', include('player.urls')),
    url(r'^$', home, name='tictactoe_welcome'),
]
