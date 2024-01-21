document.addEventListener('DOMContentLoaded', function () {
            let container = document.getElementById('nutrientInputsContainer');
            let addButton = document.getElementById('addNutrientButton');

            function saveFormState() {
                let nutrientData = [];
                container.querySelectorAll('div').forEach(div => {
                    let name = div.querySelector('input[name="nutrient_name[]"]').value;
                    let amount = div.querySelector('input[name="nutrient_amount[]"]').value;
                    nutrientData.push({name, amount});
                });
                sessionStorage.setItem('nutrientFormData', JSON.stringify(nutrientData));
            }

            function addNutrientInput(name = '', amount = '') {
                let newFieldHtml = `<div class="form-group row" style="margin-bottom: -2px">
                                        <div class="col-9 col-sm-9 col-md-6 col-auto" style="margin-right: -1em">
                                            <input type="text" name="nutrient_name[]" placeholder="Name" value="${name}" class="form-control form-control-sm">
                                        </div>
                                        <div class="col-6 col-xs-5 col-sm-6 col-md-4 col-lg-3 col-xl-3 col-auto" style="margin-right: -1em">
                                            <input type="text" name="nutrient_amount[]" placeholder="Amount" value="${amount}" class="form-control form-control-sm">
                                        </div>
                                        <div class="col-auto">
                                            <select id="content_unit" name="nutrient_unit[]" class="form-control form-control-sm">
                                                <option value="g">g</option>
                                                <option value="mg">mg</option>
                                                <option value="mg">kcal</option>
                                                <!-- Add more units as needed -->
                                            </select>
                                        </div>
                                    </div>`;
                container.insertAdjacentHTML('beforeend', newFieldHtml);

                container.querySelectorAll('input').forEach(input => {
                    input.addEventListener('change', saveFormState);
                });

            }
            addNutrientInput();
            addNutrientInput();
            addNutrientInput();
            addButton.addEventListener('click', function() {
                addNutrientInput();
            });

            if (performance.navigation.type === performance.navigation.TYPE_RELOAD) {
                sessionStorage.clear();
            }

            // Load saved form data if available
            let savedData = sessionStorage.getItem('nutrientFormData');
                if (savedData) {
                    let nutrientData = JSON.parse(savedData);
                    nutrientData.forEach(data => {
                        addNutrientInput(data.name, data.amount);
                    });
                } else {
                    // Add the first nutrient input by default
                    addNutrientInput();
                }
            });