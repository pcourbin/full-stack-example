import { Component, OnInit, InjectionToken, Inject, Optional } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { FormsModule, FormBuilder, FormGroup } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';

import { ThemeService, Theme } from '../../../SPOTAPI';

import { PORTAL_DATA } from '../overlay-with-injection.service';

@Component({
  selector: 'app-theme-form-patch',
  templateUrl: './theme-form-patch.component.html',
  styleUrls: ['./theme-form-patch.component.scss']
})
export class ThemeFormPatchComponent implements OnInit {
  public themeFormGroup: FormGroup;

  constructor(@Inject(PORTAL_DATA) public overlay, private _formBuilder: FormBuilder, private themeService: ThemeService) { }

  ngOnInit() {
      this.formBuild();
  }

  formBuild(){
    this.themeFormGroup = this._formBuilder.group({
      title:[this.overlay.object.title]
    });
  }

  onSubmitForm() {
    this.overlay.object.title = this.themeFormGroup.value.title;
    this.themeService.themesThemeIDPatch(this.overlay.object.id,this.overlay.object).subscribe();
    this.overlay.overlay.detach();
  }

}
