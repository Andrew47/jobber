jobber.controller('NewCompanyCtrl', ['companiesResourceFactory', '$window', function(companiesResourceFactory, $window) {
  var self = this;

  self.createNewCompany = function() {
    companiesResourceFactory.postCompanies(self.name, self.summary, self.website, self.industry, self.city, self.postcode, self.size, self.logo)
      .then(function() {
        $window.location.href = '/companies';
      });
  };

  self.scrapeCompanyData = function(){
    companiesResourceFactory.getCompanyFromLinkedin(self.companyURL)
      .then(function(response){
        self.scrapedData = response.data;
        self.name = response.
      });
  };
}]);
